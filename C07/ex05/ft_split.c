/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42yerevan.am>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/11 17:08:15 by vchiling          #+#    #+#             */
/*   Updated: 2025/12/11 17:56:15 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	found_in_charset(char sep, char *charset)
{
	int	i;

	i = 0;
	while (charset[i])
	{
		if (sep == charset[i])
			return (1);
		++i;
	}
	return (0);
}

int	word_count(char *str, char *charset)
{
	int	i;
	int	count;

	count = 0;
	i = 0;
	while (str[i])
	{
		if (found_in_charset(str[i], str) != found_in_charset(str[i + 1], charset))
			++count;
		++i;
	}
	return (count);
}


char	**allocate(char *str, char *charset)
{
	int		i;
	int		w_count;
	char	**strs;

	w_count = word_count(str, charset);
	strs = malloc((w_count + 1) * sizeof(char *));
	if (!strs)
		return (NULL);
	strs[w_count] = NULL;
}

char	**ft_split(char *str, char *charset)
{

