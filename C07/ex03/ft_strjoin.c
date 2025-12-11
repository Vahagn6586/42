/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42yerevan.am>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/11 14:52:04 by vchiling          #+#    #+#             */
/*   Updated: 2025/12/11 16:46:21 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		++i;
	return (i);
}

char	*ft_strcat(char *dest, char *src)
{
	char	*ret;

	ret = dest;
	while (*dest)
		dest++;
	while (*src)
	{
		*dest = *src;
		dest++;
		src++;
	}
	*dest = '\0';
	return (ret);
}

char	*allocate(int size, char **strs, char *sep)
{
	int		llen;
	int		i;
	char	*string;

	i = 0;
	llen = 0;
	if (size == 0)
	{
		string = malloc(1);
		if (!string)
			return (NULL);
		*string = '\0';
		return (string);
	}
	while (i < size)
	{
		llen += ft_strlen(strs[i]);
		++i;
	}
	string = malloc(llen + (size - 1) * ft_strlen(sep) + 1);
	if (!string)
		return (NULL);
	return (string);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		i;
	char	*string;

	string = allocate(size, strs, sep);
	if (!string)
		return (NULL);
	string[0] = '\0';
	i = 0;
	while (i < size)
	{
		ft_strcat(string, strs[i]);
		if (i < size - 1)
			ft_strcat(string, sep);
		++i;
	}
	return (string);
}
