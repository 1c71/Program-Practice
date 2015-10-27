<?php 
// http://stackoverflow.com/questions/541430/how-do-i-read-any-request-header-in-php

$all_headers = apache_request_headers();

foreach ($all_headers as $header => $value) {
    echo "$header: $value <br />\n";
}

?>