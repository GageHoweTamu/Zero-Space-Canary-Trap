# Zero-Space Canary Trap
Encodes strings like "Hi! I'm FirstName LastName" as binary zero-space character combinations, for cheater/leak detection
* Converts arbitrary strings to and from binary signatures
* Inspired by https://en.wikipedia.org/wiki/Canary_trap

### Demonstration

This is a sample output of the function. Copy/paste it into a text editor and try to navigate through the "empty" string.
```
Original Text: "Gage Howe"
Encoded text: "‌​​​‌‌‌​‌‌​​​​‌​‌‌​​‌‌‌​‌‌​​‌​‌​​‌​​​​​​‌​​‌​​​​‌‌​‌‌‌‌​‌‌‌​‌‌‌​‌‌​​‌​‌"
Decoded text: "Gage Howe"
```
