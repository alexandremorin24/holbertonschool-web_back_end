import eslintPluginJest from 'eslint-plugin-jest';

export default [
    {
        files: ['**/*.js'],
        languageOptions: {
            ecmaVersion: 2018,
            sourceType: 'module',
        },
        plugins: {
            jest: eslintPluginJest,
        },
        rules: {
            'no-console': 'off',
            'no-shadow': 'off',
            'no-restricted-syntax': [
                'error',
                'LabeledStatement',
                'WithStatement',
            ],
        },
    },
];
