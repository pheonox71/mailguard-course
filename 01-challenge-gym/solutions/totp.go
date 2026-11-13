package totp

import (
        "crypto/hmac"
        "crypto/sha1"
        "crypto/sha256"
        "crypto/sha512"
        "encoding/binary"
        "fmt"
        "hash"
        "math"
)

func Truncate(digest []byte, digits int) (string, error) {
        if digits < 6 || digits > 10 {
                return "", fmt.Errorf("digits must be 6..10")
        }
        if len(digest) < 20 {
                return "", fmt.Errorf("digest too short")
        }
        offset := int(digest[len(digest)-1] & 0x0f)
        binaryCode := (int(digest[offset]&0x7f) << 24) |
                (int(digest[offset+1]&0xff) << 16) |
                (int(digest[offset+2]&0xff) << 8) |
                int(digest[offset+3]&0xff)
        mod := int(math.Pow10(digits))
        otp := binaryCode % mod
        return fmt.Sprintf("%0*d", digits, otp), nil
}

func Generate(secret []byte, t int64, digits int, digestName string, step int64, t0 int64) (string, error) {
        if step <= 0 {
                return "", fmt.Errorf("step must be > 0")
        }
        if t < t0 {
                return "", fmt.Errorf("t < t0")
        }
        hf, err := hashFunc(digestName)
        if err != nil {
                return "", err
        }
        counter := (t - t0) / step
        var buf [8]byte
        binary.BigEndian.PutUint64(buf[:], uint64(counter))
        mac := hmac.New(hf, secret)
        mac.Write(buf[:])
        return Truncate(mac.Sum(nil), digits)
}

func hashFunc(name string) (func() hash.Hash, error) {
        switch name {
        case "sha1":
                return sha1.New, nil
        case "sha256":
                return sha256.New, nil
        case "sha512":
                return sha512.New, nil
        default:
                return nil, fmt.Errorf("unsupported digest")
        }
}
