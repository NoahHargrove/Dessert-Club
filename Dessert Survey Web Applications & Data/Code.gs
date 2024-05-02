// Function to handle GET requests and serve the HTML page from file.
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('WebApp');
}

// Function to add a new record to the Google Sheet based on dessert attributes provided.
function AddRecord(dessertName, cookie, brownie, bar, cake, parfait, pie, cupcakeMuffin, breakfast, heavy, tart, sweet, fluffy, gooey, dye, chocolate, extraChocolate, fudge, peanutButter, whiteChocolate, butterscotch, sprinkles, cinnamon, brownSugar, powederSugar, oreo, cookieDough, marshmallow, mintMocha, mAndMs, pretzels, caramel, pumpkin, banana, strawberry, blueberry, cherry, orange, lemon, carrot, differentVegetable, diffFruit) {
  // URL of the Google Sheet where data is stored
  var url = 'https://docs.google.com/spreadsheets/d/1oiK80folbw_Q3K43kFP9V1CuvQl8sHZ5SHk1AR7PUwA/edit#gid=0';
  // Open the spreadsheet by URL
  var ss = SpreadsheetApp.openByUrl(url);
  var webAppSheet = ss.getSheetByName("Sheet1");
  // Append the new row with data from the function arguments and the current date
  webAppSheet.appendRow([dessertName, cookie, brownie, bar, cake, parfait, pie, cupcakeMuffin, breakfast, heavy, tart, sweet, fluffy, gooey, dye, chocolate, extraChocolate, fudge, peanutButter, whiteChocolate, butterscotch, sprinkles, cinnamon, brownSugar, powederSugar, oreo, cookieDough, marshmallow, mintMocha, mAndMs, pretzels, caramel, pumpkin, banana, strawberry, blueberry, cherry, orange, lemon, carrot, differentVegetable, diffFruit, new Date()]);
}
