< [[05 Programming]]

- **HTML** (**H**yper**T**ext **M**arkup **L**anguage): used to create structure and content of webpage
- Most HTML elements contain `<opening>` and `</closing tags>` with raw text or other HTML tags between them
- HTML elements can be nested inside other elements. Enclosed element is child of enclosing parent element
- Any visible content should be placed within opening and closing `<body>` tags
- `<h1>` to `<h6>`: headings/sub-headings
- `<p>`, `<span>` and `<div>` specify text or blocks
- *`<em>`* and **`<strong>`**
- `<br>`: line break
- `<ol>`: ordered list; `<ul>`: unordered list
- `<img>` and `<video>` added by linking existing source

- [Codecademy Docs: HTML](https://www.codecademy.com/resources/docs/html)
- [Codecademy Workspaces: HTML](https://www.codecademy.com/workspaces/new)

1. `<!DOCTYPE html>` declaration should always be the first line of code in HTML files. This lets the browser know what version of HTML to expect.
2. `<html>` element will contain all of the HTML code
3. Information about web page, like title, belongs within `<head>` of page
4. `<title>` element, inside of head: add title to page
5. Webpage’s title appears in browser’s tab
6. Anchor tags (`<a>`) used to link internal/external pages or content on same page
7. Create sections on webpage (`id="name of section"`) and jump to them `<a href="#name of section>`
10. `<!-- comment -->`

```
<!DOCTYPE html>

<body>

  <a href="./index.html">Brown Bear</a>
  <a href="./aboutme.html">About Me</a>

  <h1>The Brown Bear</h1>
  <ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#habitat">Habitat</a></li>
    <li><a href="#media">Media</a></li>
  </ul>
  
  <div id="introduction">

    <h2>About Brown Bears</h2>
    <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern</strong>. <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
    <a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">Learn More</a>

    <h3>Species</h3>
    <ul>
      <li>Arctos</li>
      <li>Collarus</li>
      <li>Horribilis</li>
      <li>Nelsoni (extinct)</li>
    </ul>

    <h3>Features</h3>
    <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>

  </div>

  <div id="habitat">

    <h2>Habitat</h2>

    <h3>Countries with Large Brown Bear Populations</h3>
    <ol>
      <li>Russia</li>
      <li>United States</li>
      <li>Canada</li>
    </ol>
    
    <h3>Countries with Small Brown Bear Populations</h3>
    <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>

  </div>

  <div id="media">

    <h2>Media</h2>
    <a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank"><img src="https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg" /></a>
    
    <video src="https://content.codecademy.com/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4" width="320" height="240" controls>
      Video not supported
    </video>

  </div>

</body>
```

___
Tables

- `<table>`
- `<tr>`: rows
- `<td>`: data
- `<th>`: table heading
- `colspan`: attribute to make an element span over more than  1 column
- `rowspan`: attribute to make an element span over more than  1 row
- Tables can be split into three main sections:
	- `<thead>`
	- `<tbody>`
	- `<tfoot>`
- CSS properties can be applied to tables and their data
___

**[Keep learning!](https://www.codecademy.com/enrolled/courses/learn-html)**
