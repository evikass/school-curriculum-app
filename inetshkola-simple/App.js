import React, { useState } from 'react';
import { StyleSheet, Text, View, ScrollView, TouchableOpacity, SafeAreaView, StatusBar } from 'react-native';

const GRADES = [
  { id: 0, name: 'Подготовительный', subjects: ['Подготовка к письму', 'Основы счёта', 'Развитие речи', 'Окружающий мир'] },
  { id: 1, name: '1 класс', subjects: ['Русский язык', 'Математика', 'Литература', 'Окружающий мир', 'Иностранный язык'] },
  { id: 2, name: '2 класс', subjects: ['Русский язык', 'Математика', 'Литература', 'Окружающий мир', 'Иностранный язык'] },
  { id: 3, name: '3 класс', subjects: ['Русский язык', 'Математика', 'Литература', 'Окружающий мир', 'Иностранный язык', 'Информатика'] },
  { id: 4, name: '4 класс', subjects: ['Русский язык', 'Математика', 'Литература', 'Окружающий мир', 'Иностранный язык', 'Основы религии'] },
  { id: 5, name: '5 класс', subjects: ['Русский язык', 'Математика', 'Литература', 'История', 'Биология', 'География'] },
  { id: 6, name: '6 класс', subjects: ['Русский язык', 'Математика', 'Литература', 'История', 'Биология', 'География', 'Физика'] },
  { id: 7, name: '7 класс', subjects: ['Русский язык', 'Алгебра', 'Геометрия', 'Физика', 'История', 'Биология', 'География'] },
  { id: 8, name: '8 класс', subjects: ['Русский язык', 'Алгебра', 'Геометрия', 'Физика', 'Химия', 'История', 'Биология'] },
  { id: 9, name: '9 класс', subjects: ['Русский язык', 'Алгебра', 'Геометрия', 'Физика', 'Химия', 'История', 'Обществознание'] },
  { id: 10, name: '10 класс', subjects: ['Русский язык', 'Алгебра', 'Геометрия', 'Физика', 'Химия', 'История', 'Обществознание', 'Биология'] },
  { id: 11, name: '11 класс', subjects: ['Русский язык', 'Алгебра', 'Геометрия', 'Физика', 'Химия', 'История', 'Обществознание', 'Подготовка к ЕГЭ'] },
];

const COLORS = {
  background: '#0f172a',
  card: '#1e293b',
  text: '#f8fafc',
  textSecondary: '#94a3b8',
  accent: '#22d3ee'
};

const GRADE_COLORS = ['#f472b6', '#fb923c', '#facc15', '#4ade80', '#22d3ee', '#60a5fa', '#a78bfa', '#f472b6', '#fb923c', '#facc15', '#4ade80', '#22d3ee'];

export default function App() {
  const [selectedGrade, setSelectedGrade] = useState(null);

  if (selectedGrade !== null) {
    return (
      <SafeAreaView style={styles.container}>
        <StatusBar barStyle="light-content" />
        <TouchableOpacity style={styles.backButton} onPress={() => setSelectedGrade(null)}>
          <Text style={styles.backButtonText}>← Назад</Text>
        </TouchableOpacity>
        <View style={styles.header}>
          <Text style={styles.title}>{GRADES[selectedGrade].name}</Text>
        </View>
        <ScrollView style={styles.list}>
          {GRADES[selectedGrade].subjects.map((subject, index) => (
            <View key={index} style={styles.subjectCard}>
              <Text style={styles.subjectTitle}>{subject}</Text>
            </View>
          ))}
        </ScrollView>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" />
      <View style={styles.header}>
        <Text style={styles.title}>ИНЕТШКОЛА</Text>
        <Text style={styles.subtitle}>Школьная программа 0-11 класс</Text>
      </View>
      <ScrollView style={styles.list}>
        <View style={styles.grid}>
          {GRADES.map((grade) => (
            <TouchableOpacity key={grade.id} style={[styles.card, { borderColor: GRADE_COLORS[grade.id] }]} onPress={() => setSelectedGrade(grade.id)}>
              <View style={[styles.gradeNumber, { backgroundColor: GRADE_COLORS[grade.id] }]}>
                <Text style={styles.gradeNumberText}>{grade.id === 0 ? 'Д' : grade.id}</Text>
              </View>
              <Text style={styles.gradeName}>{grade.name}</Text>
              <Text style={styles.gradeSubjects}>{grade.subjects.length} предметов</Text>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  header: { padding: 20, paddingTop: 10 },
  title: { fontSize: 28, fontWeight: 'bold', color: COLORS.text, textAlign: 'center' },
  subtitle: { fontSize: 16, color: COLORS.textSecondary, textAlign: 'center', marginTop: 4 },
  backButton: { paddingHorizontal: 20, paddingTop: 10 },
  backButtonText: { color: COLORS.accent, fontSize: 16 },
  list: { flex: 1, padding: 16 },
  grid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between' },
  card: { width: '48%', backgroundColor: COLORS.card, borderRadius: 16, padding: 16, marginBottom: 16, borderWidth: 2 },
  gradeNumber: { width: 48, height: 48, borderRadius: 24, justifyContent: 'center', alignItems: 'center', marginBottom: 12 },
  gradeNumberText: { fontSize: 22, fontWeight: 'bold', color: COLORS.background },
  gradeName: { fontSize: 16, fontWeight: '600', color: COLORS.text, marginBottom: 4 },
  gradeSubjects: { fontSize: 14, color: COLORS.textSecondary },
  subjectCard: { backgroundColor: COLORS.card, borderRadius: 12, padding: 16, marginBottom: 12 },
  subjectTitle: { fontSize: 18, fontWeight: '600', color: COLORS.text },
});
