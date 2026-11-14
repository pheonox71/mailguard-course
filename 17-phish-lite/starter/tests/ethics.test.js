import { describe, it, expect } from "vitest";
import { ethicalSimOk, reportVsClickRatio, reportRate, clickRate } from "../src/lib/ethics.js";

describe("ethicalSimOk", () => {
  it("requires consent and no credential capture", () => {
    expect(ethicalSimOk({ consent: true, capturesCredentials: false })).toBe(true);
    expect(ethicalSimOk({ consent: true, capturesCredentials: true })).toBe(false);
  });
});

describe("reportVsClickRatio", () => {
  it("balances reports vs clicks", () => {
    expect(reportVsClickRatio(3, 1)).toBe(0.75);
  });
});

describe("reportRate / clickRate", () => {
  it("normalizes by delivered", () => {
    expect(reportRate(30, 100)).toBe(0.3);
    expect(clickRate(10, 100)).toBe(0.1);
  });
});
