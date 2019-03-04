from pyquery import PyQuery

from django_webtest import WebTest


class DjangoBootstrap3FormTest(WebTest):
    def test_form(self):
        # -- get example form
        page = self.app.get('/')

        # check username
        row_username = page.pyquery('#row-example-username')
        self.assertEqual(row_username.attr['class'], 'form-group required')

        username_label = row_username.find('label')
        self.assertEqual(username_label.text(), 'Username')
        self.assertEqual(username_label.attr['class'], None)
        self.assertEqual(username_label.attr['for'], 'id_example-username')

        username_input = row_username.find('#id_example-username')
        self.assertEqual(username_input.attr('class'), 'form-control')
        self.assertEqual(username_input.attr('placeholder'), 'Enter username')

        # check field 'choice'
        choice_input = page.pyquery('#id_example-choice')
        self.assertEqual(len(choice_input), 1)

        # check field 'more options'
        row_more_options = page.pyquery('#row-example-more_options')

        radio_inputs = row_more_options.find('input[type=radio]')
        self.assertEqual(len(radio_inputs), 3)
        self.assertEqual(radio_inputs[0].attrib['value'], 'abc')
        self.assertEqual(radio_inputs[0].name, 'example-more_options')

        # -- fill form and submit
        form = page.form

        form['example-username'] = 'jscott'
        form['example-password'] = 'p1'
        form['example-choice'] = True
        form['example-text'] = 'Lorem ipsum'
        form['example-options'] = 'def'
        form['example-more_options'] = 'ghi'
        form['example-date'] = '2013-12-31'

        submitted_form = form.submit().form

        # check values
        self.assertEqual(submitted_form['example-username'].value, 'jscott')
        self.assertTrue(submitted_form['example-choice'].value in ('True', 'on'))
        self.assertEqual(submitted_form['example-options'].value, 'def')
        self.assertEqual(submitted_form['example-more_options'].value, 'ghi')
        self.assertEqual(submitted_form['example-date'].value, '2013-12-31')

        # check errors
        form = self.app.get('/').form
        page = form.submit()

        row_username = page.pyquery('#row-example-username')
        self.assertEqual(row_username.attr['class'], 'form-group has-error required')
        self.assertEqual(
            PyQuery(row_username).find('.help-block').text(),
            'This field is required.'
        )
