from pyquery import PyQuery

from django_webtest import WebTest


class DjangoBootstrap3FormTest(WebTest):
    def test_form(self):
        # -- get example form
        page = self.app.get('/')

        # check username
        row_username = page.pyquery('#row-username')
        self.assertEqual(row_username.attr['class'], 'form-group required')

        username_label = row_username.find('label')
        self.assertEqual(username_label.text(), 'Username')
        self.assertEqual(username_label.attr['class'], None)

        username_input = row_username.find('#id_username')
        self.assertEqual(username_input.attr('class'), 'form-control')
        self.assertEqual(username_input.attr('placeholder'), 'Enter username')

        # check field 'choice'
        choice_input = page.pyquery('#id_choice')
        self.assertEqual(len(choice_input), 1)

        # check field 'more options'
        row_more_options = page.pyquery('#row-more_options')

        radio_inputs = row_more_options.find('input[type=radio]')
        self.assertEqual(len(radio_inputs), 3)
        self.assertEqual(radio_inputs[0].attrib['value'], 'abc')
        self.assertEqual(radio_inputs[0].name, 'more_options')

        # -- fill form and submit
        form = page.form

        form['username'] = 'jscott'
        form['password'] = 'p1'
        form['choice'] = True
        form['text'] = 'Lorem ipsum'
        form['options'] = 'def'
        form['more_options'] = 'ghi'
        form['date'] = '2013-12-31'

        submitted_form = form.submit().form

        # check values
        self.assertEqual(submitted_form['username'].value, 'jscott')
        self.assertTrue(submitted_form['choice'].value in ('True', 'on'))
        self.assertEqual(submitted_form['options'].value, 'def')
        self.assertEqual(submitted_form['more_options'].value, 'ghi')
        self.assertEqual(submitted_form['date'].value, '2013-12-31')

        # check errors
        form = self.app.get('/').form
        page = form.submit()

        row_username = page.pyquery('#row-username')
        self.assertEqual(row_username.attr['class'], 'form-group has-error required')
        self.assertEqual(
            PyQuery(row_username).find('.help-block').text(),
            'This field is required.'
        )