import adapter from "@sveltejs/adapter-auto";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    // Why adapter-auto: fine for local labs; swap for a static adapter if you deploy.
    adapter: adapter(),
  },
};

export default config;
