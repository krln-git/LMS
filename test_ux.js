const { JSDOM } = require("jsdom");
const fs = require("fs");

const dom = new JSDOM(`
<!DOCTYPE html>
<html>
<body>
  <div id="login-form"></div>
  <script type="text/template" id="login-tpl">
    <form>
      <%= context.fields %>
    </form>
  </script>
</body>
</html>
`);

console.log("JSDOM setup complete");
