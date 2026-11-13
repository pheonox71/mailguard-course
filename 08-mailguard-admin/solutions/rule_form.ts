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

export function validateRuleForm(input: RuleFormInput): RuleFormResult {
  const errors: string[] = [];
  if (!input.name.trim()) errors.push('name required');
  if (!input.decision) errors.push('decision required');
  const hasPredicate = Boolean(input.recipientDomain?.trim() || input.contains?.trim());
  if (!hasPredicate) errors.push('at least one predicate required');
  return { ok: errors.length === 0, errors };
}

export function formatHoldRow(subject: string, sender: string): string {
  return `${sender} — ${subject}`;
}
