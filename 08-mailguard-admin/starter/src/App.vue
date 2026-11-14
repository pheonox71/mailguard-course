<script setup lang="ts">
import { ref } from "vue";

/** Decision union shared with the Module 07 API contract. */
export type Decision = "hold" | "allow" | "reject";

interface HoldRow {
  id: string;
  subject: string;
  sender: string;
  decision: Decision;
}

// Why local mock rows: the starter boots without a live API; wire fetch later.
const rows = ref<HoldRow[]>([
  {
    id: "msg-1",
    subject: "Q4 forecast.xlsx",
    sender: "analyst@partner.example",
    decision: "hold",
  },
]);

function labelFor(d: Decision): string {
  return d.toUpperCase();
}
</script>

<template>
  <main class="admin">
    <h1>MailGuard Admin</h1>
    <p class="hint">
      Starter SPA — call the Module 07 API for real hold rows. Never put cloud
      secrets in this bundle.
    </p>
    <table>
      <thead>
        <tr>
          <th scope="col">Subject</th>
          <th scope="col">Sender</th>
          <th scope="col">Decision</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.id">
          <td>{{ row.subject }}</td>
          <td>{{ row.sender }}</td>
          <td>{{ labelFor(row.decision) }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>

<style scoped>
.admin {
  font-family: system-ui, sans-serif;
  max-width: 40rem;
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
</style>
