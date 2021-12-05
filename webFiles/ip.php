<?php
header("Content-Type: application/json");


$resp = $_SERVER;
unset($resp['PATH']);
unset($resp['SystemRoot']);
unset($resp['PATHTEXT']);
unset($resp['WINDIR']);
unset($resp['DOCUMENT_ROOT']);
unset($resp['CONTEXT_DOCUMENT_ROOT']);
unset($resp['COMSPEC']);
unset($resp['SERVER_ADMIN']);
unset($resp['SCRIPT_FILENAME']);
unset($resp['CONTEXT_PREFIX']);
unset($resp['ARGV']);
unset($resp['SERVER_ADDR']);
unset($resp['PHP_SELF']);
unset($resp['SCRIPT_NAME']);
unset($resp['REQUEST_TIME']);
unset($resp['LD_LIBRARY_PATH']);

ksort($resp);
echo json_encode($resp, JSON_PRETTY_PRINT);
//echo json_encode($resp);
?>

