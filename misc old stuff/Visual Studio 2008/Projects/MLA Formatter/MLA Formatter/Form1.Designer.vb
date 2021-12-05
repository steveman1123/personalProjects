<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
        Me.lblFirst = New System.Windows.Forms.Label
        Me.lblLast = New System.Windows.Forms.Label
        Me.lblTitle = New System.Windows.Forms.Label
        Me.lblCompany = New System.Windows.Forms.Label
        Me.lblYear = New System.Windows.Forms.Label
        Me.lblCopy = New System.Windows.Forms.Label
        Me.lblMessage = New System.Windows.Forms.Label
        Me.btnFormat = New System.Windows.Forms.Button
        Me.lblCity = New System.Windows.Forms.Label
        Me.txtFirst = New System.Windows.Forms.TextBox
        Me.txtLast = New System.Windows.Forms.TextBox
        Me.txtTitle = New System.Windows.Forms.TextBox
        Me.txtCity = New System.Windows.Forms.TextBox
        Me.txtCompany = New System.Windows.Forms.TextBox
        Me.txtYear = New System.Windows.Forms.TextBox
        Me.txtMLA = New System.Windows.Forms.TextBox
        Me.SuspendLayout()
        '
        'lblFirst
        '
        Me.lblFirst.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblFirst.Location = New System.Drawing.Point(0, 8)
        Me.lblFirst.Name = "lblFirst"
        Me.lblFirst.Size = New System.Drawing.Size(104, 24)
        Me.lblFirst.TabIndex = 1
        Me.lblFirst.Text = "Author's First Name"
        Me.lblFirst.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'lblLast
        '
        Me.lblLast.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblLast.Location = New System.Drawing.Point(8, 40)
        Me.lblLast.Name = "lblLast"
        Me.lblLast.Size = New System.Drawing.Size(96, 24)
        Me.lblLast.TabIndex = 1
        Me.lblLast.Text = "Author's last Name"
        Me.lblLast.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'lblTitle
        '
        Me.lblTitle.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblTitle.Location = New System.Drawing.Point(8, 72)
        Me.lblTitle.Name = "lblTitle"
        Me.lblTitle.Size = New System.Drawing.Size(96, 24)
        Me.lblTitle.TabIndex = 1
        Me.lblTitle.Text = "Title"
        Me.lblTitle.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'lblCompany
        '
        Me.lblCompany.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblCompany.Location = New System.Drawing.Point(0, 136)
        Me.lblCompany.Name = "lblCompany"
        Me.lblCompany.Size = New System.Drawing.Size(104, 24)
        Me.lblCompany.TabIndex = 1
        Me.lblCompany.Text = "Publishing Company"
        Me.lblCompany.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'lblYear
        '
        Me.lblYear.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblYear.Location = New System.Drawing.Point(0, 168)
        Me.lblYear.Name = "lblYear"
        Me.lblYear.Size = New System.Drawing.Size(104, 24)
        Me.lblYear.TabIndex = 1
        Me.lblYear.Text = "Year Published"
        Me.lblYear.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'lblCopy
        '
        Me.lblCopy.AutoSize = True
        Me.lblCopy.Location = New System.Drawing.Point(216, 8)
        Me.lblCopy.Name = "lblCopy"
        Me.lblCopy.Size = New System.Drawing.Size(146, 13)
        Me.lblCopy.TabIndex = 2
        Me.lblCopy.Text = "Copy this into your document:"
        '
        'lblMessage
        '
        Me.lblMessage.AutoSize = True
        Me.lblMessage.ForeColor = System.Drawing.Color.DarkRed
        Me.lblMessage.Location = New System.Drawing.Point(288, 152)
        Me.lblMessage.Name = "lblMessage"
        Me.lblMessage.Size = New System.Drawing.Size(165, 13)
        Me.lblMessage.TabIndex = 2
        Me.lblMessage.Text = "*n will appear if nothing is entered"
        '
        'btnFormat
        '
        Me.btnFormat.Location = New System.Drawing.Point(216, 152)
        Me.btnFormat.Name = "btnFormat"
        Me.btnFormat.Size = New System.Drawing.Size(64, 32)
        Me.btnFormat.TabIndex = 3
        Me.btnFormat.Text = "Format"
        Me.btnFormat.UseVisualStyleBackColor = True
        '
        'lblCity
        '
        Me.lblCity.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblCity.Location = New System.Drawing.Point(0, 104)
        Me.lblCity.Name = "lblCity"
        Me.lblCity.Size = New System.Drawing.Size(104, 24)
        Me.lblCity.TabIndex = 1
        Me.lblCity.Text = "Publishing City"
        Me.lblCity.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'txtFirst
        '
        Me.txtFirst.Location = New System.Drawing.Point(104, 8)
        Me.txtFirst.Name = "txtFirst"
        Me.txtFirst.Size = New System.Drawing.Size(96, 20)
        Me.txtFirst.TabIndex = 4
        '
        'txtLast
        '
        Me.txtLast.Location = New System.Drawing.Point(104, 40)
        Me.txtLast.Name = "txtLast"
        Me.txtLast.Size = New System.Drawing.Size(96, 20)
        Me.txtLast.TabIndex = 5
        '
        'txtTitle
        '
        Me.txtTitle.Location = New System.Drawing.Point(104, 72)
        Me.txtTitle.Name = "txtTitle"
        Me.txtTitle.Size = New System.Drawing.Size(96, 20)
        Me.txtTitle.TabIndex = 6
        '
        'txtCity
        '
        Me.txtCity.Location = New System.Drawing.Point(104, 104)
        Me.txtCity.Name = "txtCity"
        Me.txtCity.Size = New System.Drawing.Size(96, 20)
        Me.txtCity.TabIndex = 7
        '
        'txtCompany
        '
        Me.txtCompany.Location = New System.Drawing.Point(104, 136)
        Me.txtCompany.Name = "txtCompany"
        Me.txtCompany.Size = New System.Drawing.Size(96, 20)
        Me.txtCompany.TabIndex = 8
        '
        'txtYear
        '
        Me.txtYear.Location = New System.Drawing.Point(104, 168)
        Me.txtYear.Name = "txtYear"
        Me.txtYear.Size = New System.Drawing.Size(96, 20)
        Me.txtYear.TabIndex = 9
        '
        'txtMLA
        '
        Me.txtMLA.Location = New System.Drawing.Point(216, 24)
        Me.txtMLA.Multiline = True
        Me.txtMLA.Name = "txtMLA"
        Me.txtMLA.ReadOnly = True
        Me.txtMLA.Size = New System.Drawing.Size(240, 104)
        Me.txtMLA.TabIndex = 10
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(464, 200)
        Me.Controls.Add(Me.txtMLA)
        Me.Controls.Add(Me.txtYear)
        Me.Controls.Add(Me.txtCompany)
        Me.Controls.Add(Me.txtCity)
        Me.Controls.Add(Me.txtTitle)
        Me.Controls.Add(Me.txtLast)
        Me.Controls.Add(Me.txtFirst)
        Me.Controls.Add(Me.btnFormat)
        Me.Controls.Add(Me.lblMessage)
        Me.Controls.Add(Me.lblCopy)
        Me.Controls.Add(Me.lblYear)
        Me.Controls.Add(Me.lblCity)
        Me.Controls.Add(Me.lblCompany)
        Me.Controls.Add(Me.lblTitle)
        Me.Controls.Add(Me.lblLast)
        Me.Controls.Add(Me.lblFirst)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "Form1"
        Me.Text = "MLA Formatter"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents lblFirst As System.Windows.Forms.Label
    Friend WithEvents lblLast As System.Windows.Forms.Label
    Friend WithEvents lblTitle As System.Windows.Forms.Label
    Friend WithEvents lblCompany As System.Windows.Forms.Label
    Friend WithEvents lblYear As System.Windows.Forms.Label
    Friend WithEvents lblCopy As System.Windows.Forms.Label
    Friend WithEvents lblMessage As System.Windows.Forms.Label
    Friend WithEvents btnFormat As System.Windows.Forms.Button
    Friend WithEvents lblCity As System.Windows.Forms.Label
    Friend WithEvents txtFirst As System.Windows.Forms.TextBox
    Friend WithEvents txtLast As System.Windows.Forms.TextBox
    Friend WithEvents txtTitle As System.Windows.Forms.TextBox
    Friend WithEvents txtCity As System.Windows.Forms.TextBox
    Friend WithEvents txtCompany As System.Windows.Forms.TextBox
    Friend WithEvents txtYear As System.Windows.Forms.TextBox
    Friend WithEvents txtMLA As System.Windows.Forms.TextBox

End Class
