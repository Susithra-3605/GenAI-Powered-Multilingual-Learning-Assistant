import React from "react";
import { WebView } from "react-native-webview";

export default function PronunciationWebView() {
  return <WebView source={{ uri: "https://example.com" }} style={{ flex: 1 }} />;
}
