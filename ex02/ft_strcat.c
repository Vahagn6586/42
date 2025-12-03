char	*ft_strcat(char *dest, char *src);

char	*ft_strcat(char *dest, char *src)
{
	char	*retstr;

	retstr = dest;
	while (*dest)
		++dest;
	while (*src)
	{
		*dest = *src;
		++dest;
		++src;
	}
	*dest = '\0';
	return (retstr);
}
