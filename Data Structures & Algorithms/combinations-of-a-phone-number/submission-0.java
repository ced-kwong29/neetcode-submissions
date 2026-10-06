class Solution {
    private Map<Character, String> mapping = Map.of('2', "abc",
                                                '3', "def",
                                                '4', "ghi",
                                                '5', "jkl",
                                                '6', "mno",
                                                '7', "pqrs",
                                                '8', "tuv",
                                                '9', "wxyz");

    private List<String> allCombos = new ArrayList<>();

    private void generateCombo(String digits, String currString) {
        if (digits.isEmpty()) {
            if (!currString.isEmpty()) {
                allCombos.add(currString);
            }
            return;
        }

        String remaining = digits.substring(1);
        for (char c : mapping.get(digits.charAt(0)).toCharArray()) {
            generateCombo(remaining, currString + c);
        }
    }

    public List<String> letterCombinations(String digits) {
        generateCombo(digits, "");
        return allCombos;
    }
}
