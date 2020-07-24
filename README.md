# named_colors
A visual databse of named colors - Web colors and WX Colors with other tools. 

WX colors are in UPPER Case, and web colors are in CamelCase.

A table of named colors with names and color value is presented.

The colors can be sorted by color channel (redness, greenness, blueness), brightness,  grayness, or alphabetically.
The text colors will be opposite of the background Colors (0xffffff - color.GetRGB() )
or because gray is it's own opposite, contrast mode is half opposite (mod(r+127*s, 255),mod(g+127*s, 255), mod(b+127*s, 255)  where s is 1 or -1 )

On the todo list is :
Extended information about the color redness. greenness, grayness etc
Testing FG/BG color combos
Add person custom named colors
separating the color databases (web.wx.user1,user2 ...) in notebook 

The database and tool may eventually be helpful in designing other projects - that's why I started it.
It's also a chance to keep wxpython skills acive, always learning a new trick.

