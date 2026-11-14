<script setup lang="ts">
import { nextTick, onMounted, onUnmounted, ref, watch } from "vue";

/** Decision union shared with the Module 07 API contract. */
export type Decision = "hold" | "allow" | "reject";

interface HoldRow {
  id: string;
  subject: string;
  sender: string;
  decision: Decision;
}

// Why local mock rows: the starter boots without a live API; wire fetch later.
// Malicious subject is intentional — {{ }} text binding must not execute HTML/JS.
const rows = ref<HoldRow[]>([
  {
    id: "msg-1",
    subject: "Q4 forecast.xlsx",
    sender: "analyst@partner.example",
    decision: "hold",
  },
  {
    id: "msg-xss",
    subject: '<img src=x onerror="alert(1)">',
    sender: "attacker@evil.example",
    decision: "hold",
  },
]);

const dialogOpen = ref(false);
const pendingRow = ref<HoldRow | null>(null);
const dialogTitleId = "approve-dialog-title";
const confirmBtn = ref<HTMLButtonElement | null>(null);
const cancelBtn = ref<HTMLButtonElement | null>(null);
let previouslyFocused: HTMLElement | null = null;

function labelFor(d: Decision): string {
  return d.toUpperCase();
}

function openApprove(row: HoldRow) {
  previouslyFocused = document.activeElement as HTMLElement | null;
  pendingRow.value = row;
  dialogOpen.value = true;
}

function closeApprove() {
  dialogOpen.value = false;
  pendingRow.value = null;
  // WCAG 2.2: return focus to the control that opened the dialog.
  previouslyFocused?.focus();
  previouslyFocused = null;
}

function confirmApprove() {
  // Starter: no API yet — close after the student confirms intent.
  closeApprove();
}

function onDialogKeydown(event: KeyboardEvent) {
  if (!dialogOpen.value) return;
  if (event.key === "Escape") {
    event.preventDefault();
    closeApprove();
    return;
  }
  // Simple focus cycle between the two dialog actions (WCAG keyboard operable).
  if (event.key === "Tab" && confirmBtn.value && cancelBtn.value) {
    const focusables = [cancelBtn.value, confirmBtn.value];
    const current = document.activeElement;
    const idx = focusables.indexOf(current as HTMLButtonElement);
    event.preventDefault();
    if (event.shiftKey) {
      const next = idx <= 0 ? focusables[focusables.length - 1] : focusables[idx - 1];
      next.focus();
    } else {
      const next = idx >= focusables.length - 1 ? focusables[0] : focusables[idx + 1];
      next.focus();
    }
  }
}

watch(dialogOpen, async (open) => {
  if (open) {
    await nextTick();
    // WCAG 2.2 focus: move focus into the dialog on open (initial focus on Cancel).
    cancelBtn.value?.focus();
  }
});

onMounted(() => {
  document.addEventListener("keydown", onDialogKeydown);
});
onUnmounted(() => {
  document.removeEventListener("keydown", onDialogKeydown);
});
</script>

<template>
  <main class="admin">
    <h1>MailGuard Admin</h1>
    <p class="hint">
      Starter SPA — call the Module 07 API for real hold rows. Never put cloud
      secrets in this bundle. Subjects use text bindings (never
      <code>v-html</code>).
    </p>
    <table>
      <thead>
        <tr>
          <th scope="col">Subject</th>
          <th scope="col">Sender</th>
          <th scope="col">Decision</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.id">
          <td data-testid="hold-subject">{{ row.subject }}</td>
          <td>{{ row.sender }}</td>
          <td>{{ labelFor(row.decision) }}</td>
          <td>
            <button
              type="button"
              class="approve"
              :aria-label="`Approve release for ${row.id}`"
              @click="openApprove(row)"
            >
              Approve
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!--
      WCAG 2.2 approve dialog: role=dialog, aria-modal, labelled title,
      Escape closes, Tab cycles actions, focus moves in/out, :focus-visible ring.
    -->
    <div
      v-if="dialogOpen && pendingRow"
      class="dialog-backdrop"
      role="presentation"
      @click.self="closeApprove"
    >
      <div
        class="dialog"
        role="dialog"
        aria-modal="true"
        :aria-labelledby="dialogTitleId"
      >
        <h2 :id="dialogTitleId">Confirm approve</h2>
        <p>
          Release hold <strong>{{ pendingRow.id }}</strong>? This action is
          hard to undo.
        </p>
        <p class="dialog-subject">Subject: {{ pendingRow.subject }}</p>
        <div class="dialog-actions">
          <button ref="cancelBtn" type="button" class="secondary" @click="closeApprove">
            Cancel
          </button>
          <button ref="confirmBtn" type="button" class="danger" @click="confirmApprove">
            Confirm approve
          </button>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
.admin {
  font-family: "Source Sans 3", "Segoe UI", sans-serif;
  max-width: 48rem;
  margin: 2rem auto;
  padding: 0 1rem;
}
.hint {
  color: #444;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th,
td {
  border-bottom: 1px solid #ddd;
  text-align: left;
  padding: 0.5rem;
}
button {
  font: inherit;
  padding: 0.35rem 0.75rem;
  cursor: pointer;
  border-radius: 0.25rem;
  border: 1px solid #333;
  background: #f6f6f6;
}
button:focus-visible {
  outline: 3px solid #005fcc;
  outline-offset: 2px;
}
.approve {
  background: #e8f0fe;
}
.dialog-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: grid;
  place-items: center;
  padding: 1rem;
}
.dialog {
  background: #fff;
  max-width: 28rem;
  width: 100%;
  padding: 1.25rem;
  border-radius: 0.35rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
}
.dialog-subject {
  word-break: break-word;
  font-family: ui-monospace, monospace;
  font-size: 0.9rem;
}
.dialog-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
  margin-top: 1rem;
}
.secondary {
  background: #fff;
}
.danger {
  background: #c62828;
  color: #fff;
  border-color: #8e0000;
}
</style>
