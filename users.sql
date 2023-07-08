USE [DB_Test]
GO

/****** Object:  Table [dbo].[users]    Script Date: 08-Jul-23 7:35:37 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[users](
	[id_user] [varchar](50) NOT NULL,
	[nama_user] [varchar](max) NULL,
	[umur] [int] NULL,
	[email] [varchar](max) NULL,
	[password] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_user] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

