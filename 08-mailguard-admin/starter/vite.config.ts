import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// Why Vite: fast HMR for a small admin SPA without a heavy webpack config.
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
  },
});
