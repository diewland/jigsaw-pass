<?php
  header('Content-Type: image/png');

  // prepare data from query string
  $keys = array(
    array('id', -1),
    array('tier', 'basic'),
    array('score', 0),
    array('v', 0),
  );
  foreach ($keys as $row) {
    [$key, $default] = $row;
    $value = isset($_GET[$key]) ? $_GET[$key] : $default;
    $$key = $value;
  }
  $id += 0;
  $score += 0;
  $v += 0;

  // load img
  $path = "./pass_$tier.png";
  $img = imagecreatefrompng($path);

  // font
  $font_path = "PressStart2P-Regular.ttf";
  $color = imagecolorallocate($img, 0, 0, 0);

  // print verified + id + points
  $text_id = "#$id $$score";
  if ($v == 1) {
    $ico = imagecreatefrompng('./ico_verified.png');
    imagecopyresampled($img, $ico, 55, 105, 0, 0, 50, 50, 50, 50);
    imagettftext($img, 30, 15, 115, 147, $color, $font_path, $text_id);
  }
  else {
    imagettftext($img, 30, 15, 65, 160, $color, $font_path, $text_id);
  }

  // send to browser & release memory
  imagepng($img);
  imagedestroy($img);
?>
