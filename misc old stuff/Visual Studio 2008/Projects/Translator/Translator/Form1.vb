Public Class Translator
    'Steven Williams
    '7/19/12

    Private Sub btnConvert_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnConvert.Click

        Dim strText As String = Me.txtText.Text
        Dim strascii As String = Me.txtASCII.Text
        Dim strASCletter As String = ""
        Dim strBin As String = Me.txtBin.Text
        Dim strBinLetter As String = ""
        Dim intascii As Integer = 0
        Dim count As Integer = 0
        Dim count2 As Integer = 0
        Dim count3 As Integer = 0


Handler:
        If Me.txtASCII.TextLength > 2147483647 / 9 Or Me.txtBin.TextLength > 2147483647 Or Me.txtText.TextLength > 2147483647 / 9 Then
            MessageBox.Show("Overflow", "Error")
            Me.txtText.Text = ""
            Me.txtASCII.Text = ""
            Me.txtBin.Text = ""
            GoTo ending
        Else
            If txtText.Text = "" And Val(txtASCII.Text) = 0 And Val(txtBin.Text) = 0 Or intascii > 255 Then
                MessageBox.Show("You need to enter something valid to be translated.", "Error")
                GoTo ending
            End If
        End If


        't=text, a=ascii b=binary ↓↓
        If txtText.TextLength = 0 Then 'a or b
            If txtASCII.TextLength = 0 Then 'b
                If Me.txtBin.TextLength > 2147483647 Then GoTo Handler
                If txtBin.Text.Last() <> " " Then strBin = strBin & " "
                Do Until count = strBin.Length
                    intascii = 0
                    count2 = 128
                    Do Until strBin(count) = " "
                        intascii = intascii + count2 * Val(strBin(count))
                        count2 = count2 / 2
                        count = count + 1
                    Loop
                    If intascii > 255 Then GoTo Handler

                    strascii = strascii & intascii & " "
                    count = count + 1
                Loop
                count = 0
                Do Until count = strascii.Length 'Total ascii number (ex: 115 = s)
                    strASCletter = ""
                    'part of number (ex: 1, 1, 5 = 115)
                    Do Until strascii(count) = " "
                        strASCletter = strASCletter & strascii(count)
                        count = count + 1
                    Loop
                    'works to 65535, but binary does not.
                    If Val(strASCletter) > 255 Then GoTo Handler

                    strText = strText & ChrW(Val(strASCletter))
                    count = count + 1 'counts over the space
                Loop

            Else 'a
                If txtASCII.Text.Last() <> " " Then strascii = strascii & " "
                'a to t
                Do Until count = strascii.Length 'Total ascii numbers (ex: 115,117,118 = suv)
                    strASCletter = ""
                    'part of number (ex: 1, 1, 5 = 115)
                    Do Until strascii(count) = " "
                        strASCletter = strASCletter & strascii(count)
                        count = count + 1
                    Loop
                    'works to 65535, but binary does not.
                    If Val(strASCletter) > 255 Then GoTo Handler
                    strText = strText & ChrW(Val(strASCletter))
                    count = count + 1 'counts over the space
                Loop

                'a to b
                count = 1
                strBin = ""
                intascii = 0
                count2 = 0
                count3 = 0

                Do Until count >= strascii.Length 'go until the end
                    strASCletter = ""
                    strBinLetter = ""
                    Do Until strascii(count2) = " " 'go until the next num set
                        strASCletter = strASCletter & strascii(count2)
                        count = count + 1
                        count2 = count2 + 1
                    Loop
                    intascii = Val(strASCletter)
                    If intascii > 255 Then GoTo handler
                    count3 = 128
                    Do Until count3 = 0 'go until ascNum is in bin
                        strBinLetter = strBinLetter & intascii \ count3
                        intascii = intascii Mod count3
                        count3 = count3 / 2
                    Loop
                    count = count + 1
                    count2 = count2 + 1
                    strBin = strBin & strBinLetter & " "
                Loop

            End If
        Else 't
            strascii = ""
            't to a
            Do Until count = strText.Length
                intascii = AscW(strText.Chars(count))
                If intascii > 255 Then GoTo Handler
                strascii = strascii & intascii & " "
                count = count + 1
            Loop
            'a to b (t to a already happened)
            count = 1
            strBin = ""
            intascii = 0
            count2 = 0
            Do Until count >= strascii.Length 'go until the end
                strASCletter = ""
                strBinLetter = ""
                Do Until strascii(count2) = " " 'go until the next num set
                    strASCletter = strASCletter & strascii(count2)
                    count = count + 1
                    count2 = count2 + 1
                Loop
                intascii = Val(strASCletter)
                count3 = 128
                Do Until count3 = 0 'go until ascNum is in bin
                    strBinLetter = strBinLetter & intascii \ count3
                    intascii = intascii Mod count3
                    count3 = count3 / 2
                Loop
                count = count + 1
                count2 = count2 + 1
                strBin = strBin & strBinLetter & " "
            Loop
        End If

        If Me.txtASCII.TextLength > 2147483647 / 9 Or Me.txtBin.TextLength > 2147483647 Or Me.txtText.TextLength > 2147483647 / 9 Then
            MessageBox.Show("Overflow", "Error")
            Me.txtText.Text = ""
            Me.txtASCII.Text = ""
            Me.txtBin.Text = ""
        End If

        Me.txtText.Text = strText
        Me.txtASCII.Text = strascii
        Me.txtBin.Text = strBin
ending:
    End Sub

    Private Sub mnuwhat_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles mnuwhat.Click
        MessageBox.Show("This program translates between normal text, ASCII code, and binary.", "What Is This?")
    End Sub

    Private Sub mnuAbASCII_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles mnuAbASCII.Click
        Dim count As Integer = 1
        Dim count20 As Integer = 20
        Dim strASC As String = ""
        MessageBox.Show("American Standard Code for Information Interchange (ASCII)" & vbCrLf & "is the numeraric system that computers use to code characters in." & vbCrLf & " Press 'OK' to see a chart of the 255 characters.", "About ASCII")
        Do Until count20 > 255
            strASC = ""
            Do While count <= count20
                strASC = strASC & count & "   =   " & ChrW(count) & vbCrLf
                count = count + 1
            Loop
            If count20 = 240 Then
                count20 = count20 + 15
                MessageBox.Show(strASC & vbCrLf & "Press 'OK' for the last 15", "ASCII List")
            ElseIf count20 = 255 Then
                MessageBox.Show(strASC, "ASCII List")
                count20 = count20 + 1 'ends the loop
            Else
                count20 = count20 + 20
                MessageBox.Show(strASC & vbCrLf & "Press 'OK' for the next 20", "ASCII List")
            End If
        Loop
    End Sub

    Private Sub AbBinary_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AbBinary.Click
        MessageBox.Show("Since computers are not capable of understanding high number systems, such as 0-9 (base 10), we convert it to binary, 0-1 (base 2) which it understands in the form of switches, off=0, on=1. Using different switch combinations, we make numbers, which are the ASCII numbers.", "About Binary")
    End Sub
End Class