package totp

import (
	"fmt"
	"hash"
)

// Truncate implements RFC 4226 §5.3 dynamic truncation.
func Truncate(digest []byte, digits int) (string, error) {
	panic("implement Truncate")
}

// Generate returns an RFC 6238 TOTP for unix time t.
func Generate(secret []byte, t int64, digits int, digestName string, step int64, t0 int64) (string, error) {
	panic("implement Generate")
}

func hashFunc(name string) (func() hash.Hash, error) {
	return nil, fmt.Errorf("implement hashFunc")
}
