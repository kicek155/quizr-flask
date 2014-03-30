# -*- coding: utf-8 -*-
"""
Quizr - tests.
"""
import os
import quizr
import unittest
import tempfile


class QuizrTestCase(unittest.TestCase):

    def setUp(self):
        quizr.app.config['TESTING'] = True
        self.client = quizr.app.test_client()

    def tearDown(self):
        del quizr.app.config['TESTING']

    def test_welcome_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>Quizr</h1>', resp.data)
        self.assertIn('<input type="text" name="username" />', resp.data)
        self.assertNotIn('Pole nie może być puste!', resp.data)

    def test_welcome_page_empty_username(self):
        resp = self.client.post('/', data={'username': ''})
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<input type="text" name="username" />', resp.data)
        self.assertIn('Pole nie może być puste!', resp.data)

    def test_welcome_page_start(self):
        username = 'TEST'
        resp = self.client.post('/', data={'username': username})
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.headers['Location'].endswith('/pytanie'))
        
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<p>Witaj, {0}</p>'.format(username), resp.data)

    def test_question_page(self):
        resp = self.client.get('/pytanie')
        self.assertEqual(resp.status_code, 200)

    def test_result_page(self):
        resp = self.client.get('/wynik')
        self.assertEqual(resp.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
