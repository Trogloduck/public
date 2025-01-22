<?php
// Asks user if they prefer humans, unicorns or platypuses
// Displays a gif according to answer
// human gif: https://giphy.com/embed/KzGCAlMiK6hQQ
// unicorn gif: https://giphy.com/embed/HULqwwF5tWKznstIEE
// platypus gif: https://giphy.com/embed/FNpAjwtN1p1Yc

// ask user if they're a human, unicorn or platypus with a radio form question
echo '<form action="index.php" method="post">
    <label for="answer">Do you prefer humans, unicorns or platypuses?</label><br>
    <input type="radio" id="human" name="answer" value="human">
    <label for="human">Humans</label><br>
    <input type="radio" id="unicorn" name="answer" value="unicorn">
    <label for="unicorn">Unicorns</label><br>
    <input type="radio" id="platypus" name="answer" value="platypus">
    <label for="platypus">Platypuses</label><br><br>
    <input type="submit" value="Submit">';

// display gif according to user's answer
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $answer = $_POST["answer"];
    $gif = ($answer == "human") ? "https://giphy.com/embed/KzGCAlMiK6hQQ" : (($answer == "unicorn") ? "https://giphy.com/embed/HULqwwF5tWKznstIEE" : "https://giphy.com/embed/FNpAjwtN1p1Yc");
    // display gif
    echo "<iframe src='$gif' width='480' height='270' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>";
}
?>