import App from './routes/+page.svelte'

const target = document.getElementById('app')
if (target) {
  // Svelte 5 mount
  const { mount } = await import('svelte')
  mount(App, { target })
}
