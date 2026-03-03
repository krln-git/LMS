const { JSDOM } = require("jsdom");
const fs = require('fs');

// Mock a simple DOM and necessary globals for RequireJS environment
const dom = new JSDOM(`<!DOCTYPE html><html><body></body></html>`);
global.window = dom.window;
global.document = dom.window.document;
global.gettext = (text) => text;

// Provide a basic define for RequireJS
let moduleCallback;
global.define = (deps, callback) => {
    moduleCallback = callback;
};
global.RequireJS = { define: global.define };

// Read and execute the enrollment.js script
const code = fs.readFileSync('lms/static/js/student_account/enrollment.js', 'utf8');
eval(code);

// Run the module, mocking $ and $.cookie
const mockJQuery = () => {};
mockJQuery.cookie = () => 'mock_csrf_token';

const EnrollmentInterface = moduleCallback(mockJQuery, mockJQuery.cookie);

// Test showMessage with malicious payload
const maliciousPayload = "<script>alert('xss')</script>";
EnrollmentInterface.showMessage(maliciousPayload);

// Assertions
const messageContent = document.querySelector('.message-content');
const innerHTML = messageContent.innerHTML;
const textContent = messageContent.textContent;

console.log("innerHTML of message container:", innerHTML);
console.log("textContent of message container:", textContent);

if (innerHTML === maliciousPayload) {
    console.error("❌ FAILED: XSS payload was injected as raw HTML!");
    process.exit(1);
} else if (innerHTML === "&lt;script&gt;alert('xss')&lt;/script&gt;") {
    console.log("✅ SUCCESS: HTML was correctly escaped by using textContent.");
    process.exit(0);
} else {
    console.error("❌ FAILED: Unexpected innerHTML: " + innerHTML);
    process.exit(1);
}
