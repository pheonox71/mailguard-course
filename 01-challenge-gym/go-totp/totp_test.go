package totp

import "testing"

func TestSHA1AppendixB(t *testing.T) {
        seed := []byte("12345678901234567890")
        cases := []struct {
                ts   int64
                want string
        }{
                {59, "94287082"},
                {1111111109, "07081804"},
                {1111111111, "14050471"},
                {1234567890, "89005924"},
                {2000000000, "69279037"},
                {20000000000, "65353130"},
        }
        for _, c := range cases {
                got, err := Generate(seed, c.ts, 8, "sha1", 30, 0)
                if err != nil {
                        t.Fatal(err)
                }
                if got != c.want {
                        t.Fatalf("t=%d got %s want %s", c.ts, got, c.want)
                }
        }
}
