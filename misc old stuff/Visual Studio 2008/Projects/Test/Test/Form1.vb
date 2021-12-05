Public Class Form1

    Private Sub btnEncrypt_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnEncrypt.Click
        Dim oldbase As Integer = 62
        Dim newbase As Integer = 36
        Dim counter As Integer = 0
        Dim length As Integer = 0
        Dim totalcount As Integer = 0
        Dim strmessage As String = Trim(Me.txtMessage.Text) & " "
        Dim chrmessage As Char = ""
        Dim b10 As Long = 0
        Dim chrval As Integer = 0
        Dim strOut As String = ""

        Do Until totalcount >= strmessage.Length
            b10 = 0
            length = 0
            Do Until chrmessage = " "
                chrmessage = strmessage(length)
                If chrmessage <> " " Then length = length + 1
            Loop
            totalcount = totalcount + length + 1

            For counter = 0 To length
                If Asc(strmessage(counter)) >= 48 And Asc(strmessage(counter)) <= 57 Then chrval = Asc(strmessage(counter)) - 48
                If Asc(strmessage(counter)) >= 65 And Asc(strmessage(counter)) <= 90 Then chrval = Asc(strmessage(counter)) - 55
                If Asc(strmessage(counter)) >= 97 And Asc(strmessage(counter)) <= 122 Then chrval = Asc(strmessage(counter)) - 61
                b10 = b10 + chrval * oldbase ^ ((length - counter) - 1)
            Next
            b10 = b10 - 1
            strOut = strOut & b10 & " "
            MessageBox.Show(strOut)







        Loop
    End Sub
End Class