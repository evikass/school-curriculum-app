import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>ИНЕТШКОЛА</Text>
      <Text style={styles.subtitle}>Тестовая версия</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1E1B4B',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FCD34D',
  },
  subtitle: {
    fontSize: 16,
    color: '#C4B5FD',
    marginTop: 8,
  },
});
