import { expect, test } from "@playwright/test";

test("home shows SIMULATION label and consent gate", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("status").first()).toContainText("SIMULATION");
  await expect(page.getByRole("heading", { name: /Phish Lite/i })).toBeVisible();
  await expect(page.getByRole("button", { name: /I understand/i })).toBeVisible();
});
