<?php
// This script simulates the cleanup process of a room by changing its state step by step.

// different states of the room
$possible_states = [
    1=> "nuclear wasteland",
    2=> "biohazard",
    3=> "post flood",
    4=> "war zone",
    5=> "normal",
    6=> "neat",
    7=> "shiny",
];

// current state of the room
$room_state_index = 1;
$room_state = $possible_states[$room_state_index];

// increments room_state_index by 1 and updates room_state accordingly
function clean_room($room_state_index, $possible_states) {
    if($room_state_index < 7) {
        $room_state_index++;
    }
    $room_state = $possible_states[$room_state_index];
    return [$room_state, $room_state_index];
}

// checks room_state, makes a statement about room_state, clean_room, update room_state, makes new statement
while ($room_state_index <= 7) {
    if ($room_state_index == 1) {
        echo "The room is a {$room_state}. Call the hazmats .<br>";
        list($room_state, $room_state_index) = clean_room($room_state_index, $possible_states);
    } else if ($room_state_index == 2) {
        echo "The room is {$room_state}. Call the CDC.<br>";
        list($room_state, $room_state_index) = clean_room($room_state_index, $possible_states);
    } else if ($room_state_index == 3) {    
        echo "The room is {$room_state}. Call the plumbers.<br>";
        list($room_state, $room_state_index) = clean_room($room_state_index, $possible_states);
    } else if ($room_state_index == 4) {    
        echo "The room is {$room_state}. Call the army.<br>";
        list($room_state, $room_state_index) = clean_room($room_state_index, $possible_states);
    } else if ($room_state_index == 5) {    
        echo "The room is {$room_state}. It's time to clean it up.<br>";
        list($room_state, $room_state_index) = clean_room($room_state_index, $possible_states);
    } else if ($room_state_index == 6) {    
        echo "The room is {$room_state}. It's time to clean it up.<br>";
        list($room_state, $room_state_index) = clean_room($room_state_index, $possible_states);
    } else if ($room_state_index == 7) {    
        echo "The room is {$room_state}. Good job!<br>";
        break;
    }
}
?>