import { describe, expect, it } from "vitest";
import { ethicalSimOk, reportRate } from "../src/lib/ethics.js";

describe("ethicalSimOk", () => {
  it("allows consented sims that never capture credentials", () => {
    expect(ethicalSimOk({ consent: true, capturesCredentials: false })).toBe(true);
  });

  it("fails when credential capture is enabled", () => {
    // Why fail closed: temporary “demo harvesters” must not ship.
    expect(ethicalSimOk({ consent: true, capturesCredentials: true })).toBe(false);
  });

  it("fails without consent", () => {
    expect(ethicalSimOk({ consent: false, capturesCredentials: false })).toBe(false);
  });
});

describe("reportRate", () => {
  it("uses reported / (reported + clicked)", () => {
    expect(reportRate(3, 1)).toBe(0.75);
  });
});
