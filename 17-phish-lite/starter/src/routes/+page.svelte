<script lang="ts">
  // Why consent gate: training must disclose purpose before any scenario UI.
  let consented = $state(false);

  function acceptConsent() {
    consented = true;
  }
</script>

<main class="train">
  <p class="sim-banner" role="status">SIMULATION — training only. No real credentials.</p>

  {#if !consented}
    <section aria-labelledby="consent-heading">
      <h1 id="consent-heading">Phish Lite (lab)</h1>
      <p>
        This app is an <strong>awareness simulation</strong> for a course lab. It must never
        collect passwords or session cookies from a real identity provider page.
      </p>
      <button type="button" onclick={acceptConsent}>I understand — continue</button>
    </section>
  {:else}
    <section aria-labelledby="scenario-heading">
      <h1 id="scenario-heading">Scenario list</h1>
      <p class="sim-banner" role="status">SIMULATION</p>
      <p>
        Wire scenarios next. Prefer <em>report rate</em> and time-to-report over vanity
        click-through metrics. See the Module 17 scoring kata.
      </p>
    </section>
  {/if}
</main>

<style>
  .train {
    font-family: Georgia, "Times New Roman", serif;
    max-width: 36rem;
    margin: 2rem auto;
    padding: 0 1rem;
    line-height: 1.5;
  }
  .sim-banner {
    background: #f3f0e8;
    border-left: 4px solid #8a5a2b;
    padding: 0.5rem 0.75rem;
    font-weight: 700;
    letter-spacing: 0.04em;
  }
  button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    font: inherit;
    cursor: pointer;
  }
</style>
