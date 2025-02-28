<?php

// create array of 10 random countries with their ISO code as key and name as value
$countries = array(
    'BE' => 'Belgium',
    'FR' => 'France',
    'DE' => 'Germany',
    'IT' => 'Italy',
    'LU' => 'Luxembourg',
    'NL' => 'Netherlands',
    'PT' => 'Portugal',
    'ES' => 'Spain',
    'SE' => 'Sweden',
    'UK' => 'United Kingdom'
);

// html select form with the iso code as value and the country name as text
echo '<form action="index.php" method="post">';
echo '<select name="country">';
foreach ($countries as $iso => $country) {
    echo "<option value=\"$iso\">$country</option>";
}
echo '</select>';

?>