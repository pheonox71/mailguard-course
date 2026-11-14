import { createApp } from "vue";
import App from "./App.vue";

// Why createApp: Vue 3 mounts one root component; keep API base URL out of secrets.
createApp(App).mount("#app");
