<?php
  header('Content-Type: image/png');

  // prepare data from query string
  $keys = array(
    array('tier', 'basic'),
    array('score', 0),
  );
  foreach ($keys as $row) {
    [$key, $default] = $row;
    $value = isset($_GET[$key]) ? $_GET[$key] : $default;
    $$key = $value;
  }
  $score += 0;

  // load img
  $path = "./pass_$tier.png";
  $img = imagecreatefrompng($path);

  // print point
  $text = "Points $score";
  $color = imagecolorallocate($img, 0, 0, 0);
  $font_path = "PressStart2P-Regular.ttf";
  imagettftext($img, 30, 0, 10, 50, $color, $font_path, $text);

  // send to browser & release memory
  imagepng($img);
  imagedestroy($img);
?>
