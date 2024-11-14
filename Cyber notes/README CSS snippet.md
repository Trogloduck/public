I use the following CSS snippet to modify the alignment of preview elements as there is no built-in function for that on Obsidian:

```
div[src$="#right"] {
    text-align:right;
}

div[src$="#left"] {
    text-align:left;
}

div[src$="#center"] {
    text-align:center;
}
```

If you want to be able to use that snippet, follow these steps:
1. Go to Settings > Appearance > CSS snippets, you can then open the folder containing your snippets and add all the snippets you want
2. In that folder, create a .css file in which you copy and paste the above code, save the file
3. Make sure the snippet is activated in Settings > Appearance > CSS snippets
4. Enjoy!

As you can see in this example, adding `#center` centers the image (you can't see that if you haven't added the snippet) 
You can also modify the size of an image with the pipe "`|`"

![[Pasted image 20240912150855.png#center | 400]]

