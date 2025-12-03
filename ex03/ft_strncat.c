char	*ft_strncat(char *dest, char *src, unsigned int nb);

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	char	*retstr;

	retstr = dest;
	while (*dest)
		++dest;
	while (*src && nb > 0)
	{
		*dest = *src;
		++dest;
		++src;
		--nb;
	}
	*dest = '\0';
	return (retstr);
}
