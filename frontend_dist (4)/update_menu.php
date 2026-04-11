<?php
/**
 * Webhook Receiver for Static Site Generation (Option 3)
 * This script is called by the FastAPI backend whenever a dish/category is updated in the Admin panel.
 * It fetches the fresh menu from the backend and saves it as a static menu.json file on this fast Plesk server.
 */

// Simple security token to prevent unauthorized triggers
$SECRET_TOKEN = "umai_cache_update_2026";

if (!isset($_GET['token']) || $_GET['token'] !== $SECRET_TOKEN) {
    http_response_code(403);
    die("Unauthorized access.");
}

// 1. Fetch the latest menu from our Render backend
$api_url = "https://umai-rest-backend.onrender.com/api/menu";

// Create context to allow fetching from https
$context = stream_context_create(array(
    "http" => array(
        "header" => "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64)",
        "timeout" => 60 // Wait up to 60 seconds if Render is 'sleeping'
    )
));

$menu_json = file_get_contents($api_url, false, $context);

if ($menu_json === FALSE) {
    http_response_code(500);
    die("Failed to fetch menu from backend.");
}

// Check if response is actually valid JSON
if (json_decode($menu_json) === null) {
    http_response_code(500);
    die("API did not return valid JSON.");
}

// 2. Save it directly to the Plesk hosting as menu.json
$bytes = file_put_contents('menu.json', $menu_json);

if ($bytes === false) {
    http_response_code(500);
    die("Failed to write to menu.json on Plesk server. Check file permissions.");
}

http_response_code(200);
echo "Successfully updated menu.json cache! ($bytes bytes)";
?>
