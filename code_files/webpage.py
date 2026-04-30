<!DOCTYPE html>
<html>
<head>
  <title>Raspberry Pi Car Control</title>
  <style>
    body { background:#111; color:#fff; text-align:center; font-family:Arial; }
    h1 { margin-top:30px; }
    button {
      width:120px; height:60px; margin:10px;
      font-size:18px; border-radius:10px; border:none; cursor:pointer;
    }
    .f{background:#4CAF50} .b{background:#f44336}
    .l{background:#2196F3} .r{background:#FF9800}
    .s{background:#9E9E9E}
  </style>
</head>
<body>
  <h1>🚗 Raspberry Pi Controller</h1>

  <div><button class="f" onclick="send('forward')">Forward</button></div>

  <div>
    <button class="l" onclick="send('left')">Left</button>
    <button class="s" onclick="send('stop')">Stop</button>
    <button class="r" onclick="send('right')">Right</button>
  </div>

  <div><button class="b" onclick="send('backward')">Backward</button></div>

  <script>
    function send(cmd){
      fetch('http://' + location.hostname + ':5000/' + cmd)
        .catch(e => console.log(e));
    }
  </script>
</body>
</html>