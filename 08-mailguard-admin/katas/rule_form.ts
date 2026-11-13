export type Decision = 'hold' | 'allow' | 'reject';

export interface RuleFormInput {
  name: string;
  decision: Decision | '';
  recipientDomain?: string;
  contains?: string;
}

export interface RuleFormResult {
  ok: boolean;
  errors: string[];
}

/** Validate a rule form before POST to the API. */
export function validateRuleForm(input: RuleFormInput): RuleFormResult {
  throw new Error('implement validateRuleForm');
}

/** Format a hold-queue row for display (no raw HTML). */
export function formatHoldRow(subject: string, sender: string): string {
  throw new Error('implement formatHoldRow');
}
