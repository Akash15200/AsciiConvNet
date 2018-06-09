/**
 * Letters.
 *
 * Draws letters to the screen. This requires loading a font,
 * setting the font, and then drawing the letters.
 */
PFont f;
void setup() {
  size(571, 161);
  // Create the font
  printArray(PFont.list());
  noLoop();
}

void draw() {
  background(0);
  // Set the left and top margin
  int margin = 15;
  translate(margin, margin);
  int gap = 30 ;
  for (int i = 1 ; i < PFont.list().length; i ++){
    background(0);
    f = createFont(PFont.list()[i], 30);
    textFont(f);
    textAlign(CENTER, CENTER);
    int counter = 35;
    for (int y = 0; y < height-gap; y += gap) {
        for (int x = 0; x < width-gap; x += gap) {
            char letter = char(counter);
            fill(255);
            // Draw the letter to the screen
            text(letter, x, y);
            // Increment the counter
            counter++;
        }
    }
    saveFrame("dataset/"+str(i)+".png");
  }
}
