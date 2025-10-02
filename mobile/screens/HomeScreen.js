import React from "react";
import { View, Text, Button } from "react-native";

export default function HomeScreen({ navigation }) {
  return (
    <View style={{ padding: 20 }}>
      <Text>Select a language and lesson:</Text>
      <Button title="Go to Lesson" onPress={() => navigation.navigate('LessonScreen')} />
    </View>
  );
}
