from katas.dmarc_aggregate import parse_aggregate, classify_source, next_policy_step

SAMPLE = """
<feedback>
  <record>
    <row>
      <source_ip>203.0.113.5</source_ip>
      <count>3</count>
      <policy_evaluated>
        <disposition>none</disposition>
        <dkim>pass</dkim>
        <spf>fail</spf>
      </policy_evaluated>
    </row>
  </record>
  <record>
    <row>
      <source_ip>198.51.100.9</source_ip>
      <count>10</count>
      <policy_evaluated>
        <disposition>reject</disposition>
        <dkim>fail</dkim>
        <spf>fail</spf>
      </policy_evaluated>
    </row>
  </record>
</feedback>
"""

def test_parse():
    rows = parse_aggregate(SAMPLE)
    assert len(rows) == 2
    assert rows[0].source_ip == "203.0.113.5"

def test_classify():
    rows = parse_aggregate(SAMPLE)
    assert classify_source(rows[0]) == "aligned"
    assert classify_source(rows[1]) == "spoof"

def test_next_policy():
    assert next_policy_step("none") == "quarantine"
    assert next_policy_step("reject") == "reject"
