import React from "react";
import { View, Text } from "react-native";

export default function ParentDashboard() {
  return (
    <View style={{ padding: 20 }}>
      <Text>Parent can view child's progress here.</Text>
    </View>
  );
}
