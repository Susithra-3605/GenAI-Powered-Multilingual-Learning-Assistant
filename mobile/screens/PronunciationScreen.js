import React from "react";
import { View } from "react-native";
import PronunciationWebView from "../components/PronunciationWebView";

export default function PronunciationScreen() {
  return (
    <View style={{ flex: 1 }}>
      <PronunciationWebView />
    </View>
  );
}
