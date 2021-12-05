Public Class Form1


    Private Sub btnFormat_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnFormat.Click

        Dim italic As New Font("System.Drawing.Font", 12, FontStyle.Italic)

        Dim strFirst As String = txtFirst.Text
        Dim strlast As String = txtLast.Text
        Dim strtitle As String = txtTitle.Text
        Dim strCity As String = txtCity.text
        Dim strcompany As String = txtCompany.Text
        Dim stryear As String = txtYear.Text

        If strFirst = "" Then strFirst = "n"
        If strlast = "" Then strlast = "n"
        If strtitle = "" Then strtitle = "n"
        If strCity = "" Then strCity = "n"
        If strcompany = "" Then strcompany = "n"
        If stryear = "" Then stryear = "n"

        Me.txtMLA.Text = strlast & ", " & strFirst & ". " & strtitle & ". " & strCity & ": " & strcompany & ", " & stryear



    End Sub

End Class
