chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extract_text") {
        let text = document.body.innerText;
        sendResponse({ text: text });
    }
});