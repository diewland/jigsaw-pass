<?php
  header('Content-Type: image/png');

  // prepare data from query string
  $keys = array(
    array('tier', 'basic'),
    array('score', 0),
    array('v', 0),
  );
  foreach ($keys as $row) {
    [$key, $default] = $row;
    $value = isset($_GET[$key]) ? $_GET[$key] : $default;
    $$key = $value;
  }
  $score += 0;
  $v += 0;

  // load img
  $path = "./pass_$tier.png";
  $img = imagecreatefrompng($path);

  // print point
  $text = "Points $score";
  $color = imagecolorallocate($img, 0, 0, 0);
  $font_path = "PressStart2P-Regular.ttf";
  imagettftext($img, 30, 0, 10, 50, $color, $font_path, $text);

  // print verified
  if ($v == 1) {
    $ico = imagecreatefrompng('./ico_verified.png');
    imagecopyresampled($img, $ico, 435, 430, 0, 0, 75, 75, 75, 75);
  }

  // send to browser & release memory
  imagepng($img);
  imagedestroy($img);
?>
